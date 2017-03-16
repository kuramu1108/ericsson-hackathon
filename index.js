var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight* .8 );
document.body.appendChild( renderer.domElement );

var orbit = new THREE.OrbitControls( camera, render.domElement);
orbit.enableZoom = false;

var fired_areas = [];

var lights = [];
lights[ 0 ] = new THREE.PointLight( 0xffffff, 1, 0 );
lights[ 1 ] = new THREE.PointLight( 0xffffff, 1, 0 );
lights[ 2 ] = new THREE.PointLight( 0xffffff, 1, 0 );

lights[ 0 ].position.set( 0, 200, 0 );
lights[ 1 ].position.set( 0, 0, 100 );
lights[ 2 ].position.set( - 100, - 200, - 100 );

scene.add( lights[ 0 ] );
scene.add( lights[ 1 ] );
scene.add( lights[ 2 ] );

var exits = [
    [0, 3],[11, 3]
];

var boundaries = [    
    [11, 0],
    [10, 0],
    [9, 0], [9, 2], [9, 3],
    [8, 2], [8, 3],
    [7, 0],
    [6, 0],
    [5, 0],[5,3],
    [4, 0],[4,2],[4,3],
    [3, 2],[3, 3],
    [2, 0],[2, 2],[2, 3],
    [1, 0],[1, 2],[1, 3],
    [0, 0]
];

var roomCounter = 0;
var rooms = [
    [3,0],[8,0],[5, 2]
];

function belongsTo(x, y, arr) {
    for (var i = 0; i < arr.length; i++) {
        if (x == arr[i][0] && y == arr[i][1])
            return true;
    }
}

function isBoundary(x, y) {
    for (var i = 0; i < boundaries.length; i++) {
        if (x == boundaries[i][0] && y == boundaries[i][1])
            return true;
    };
}

function isRoom(x, y) {
    for (var i = 0; i < rooms.length; i++) {
        if (x == rooms[i][0] && y == rooms[i][1])
            return true;
    };
}

for (var x = 0; x < 12; x++) {
    for (var y = 0; y < 4; y++) {
            var geometry = new THREE.BoxGeometry( 1, 1, 1 );

            
            if ( belongsTo(x, y, exits)) {
                var material = new THREE.MeshPhongMaterial( {
                    color: 0x00ff00,
                    emissive: 0x072534,
                    shading: THREE.FlatShading
                } );
                var cube = new THREE.Mesh( geometry, material );
            } else if ( belongsTo(x, y, boundaries)) {
                var material = new THREE.MeshPhongMaterial( {
                    color: 0x808080,
                    shading: THREE.FlatShading
                } );
                var cube = new THREE.Mesh( geometry, material );
            } else if ( belongsTo(x, y, rooms)) {
                var material = new THREE.MeshPhongMaterial( {
                    color: 0x0000ff,
                } );
                var cube = new THREE.Mesh( geometry, material );
            } else {
                var wireframe = new THREE.MeshBasicMaterial({
                    wireframe: true
                });
                var cube = new THREE.Mesh( geometry, wireframe );
            }
            cube.position.x = x - 6;
            cube.position.y = y - 2;
            scene.add( cube );
    }
}

camera.position.z = 15;

function render() {
    showPathWay();
	requestAnimationFrame( render );
	renderer.render( scene, camera );
}


// pathways
var pathCounter = 0;
var path = [
    [3, 1], [2, 1], [1, 1], [0, 1], [0, 2]
];

var pathway = new THREE.Mesh(
    new THREE.BoxGeometry(1, 1, 1),
    new THREE.MeshPhongMaterial({
        color: 0xffff00,
    })
);

// hazardous area block
var fireOn = false;
var fire = new THREE.Mesh(
    new THREE.BoxGeometry(1, 1, 1),
    new THREE.MeshPhongMaterial({
        color: 0xff0000
    })
);

// render exit route function
function showPathWay() {
    scene.remove(pathway);
    pathway.position.x = path[Math.floor(pathCounter)][0] - 6;
    pathway.position.y = path[Math.floor(pathCounter)][1] - 2;
    scene.add(pathway);
        
    if (pathCounter < path.length-.1)
        pathCounter+=.1
    else
        pathCounter = 0;
}

// event simulation
function simulateFire() {
    if (fireOn) {
        scene.remove(fire);
    } else {
        fire.position.x = 1 - 6;
        fire.position.y = 1 - 2;
        scene.add(fire);
    }
    fireOn = !fireOn;
    pathCounter = 0;

    pathFind();
}


// grid finding library from https://github.com/qiao/PathFinding.js
// use A* algorithm for now
function initMap() {
    var grid = new PF.Grid(12, 4);
    for (var i = 0; i < boundaries.length; i++) {
        grid.setWalkableAt(boundaries[i][0], boundaries[i][1], false);
    }
    return grid;
}



function pathFind() {
    grid = initMap();
    var finder = new PF.AStarFinder();
    var pathLength = 9999;
    if (fireOn) {
        for (var i = 0; i < exits.length; i++) {
            grid.setWalkableAt(1, 1, false);
            console.log(i);
            var evacuationPath = finder.findPath(rooms[roomCounter][0], rooms[roomCounter][1], exits[i][0], exits[i][1], grid);
            if (evacuationPath.length != 0) {
                if (evacuationPath.length < pathLength) {
                    pathLength = evacuationPath.length;
                    path = evacuationPath;
                }
            }
            grid = initMap();
        }
    } else {
        for (var i = 0; i < exits.length; i++) {
            grid.setWalkableAt(1, 1, true);
            var evacuationPath = finder.findPath(rooms[roomCounter][0], rooms[roomCounter][1], exits[i][0], exits[i][1], grid);
            if (evacuationPath.length != 0) {
                if (evacuationPath.length < pathLength) {
                    pathLength = evacuationPath.length;
                    path = evacuationPath;
                }
            }
            grid = initMap();
        }
    }
}

function room_one () {
    roomCounter = 0;
    pathCounter = 0;
    pathFind();
} 

function room_two() {
    roomCounter = 1;
    pathCounter = 0;
    pathFind();
}

function room_three () {
    roomCounter = 2;
    pathCounter = 0;
    pathFind();
}

render();