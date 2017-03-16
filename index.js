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
lights[ 1 ].position.set( 100, 200, 100 );
lights[ 2 ].position.set( - 100, - 200, - 100 );

scene.add( lights[ 0 ] );
scene.add( lights[ 1 ] );
scene.add( lights[ 2 ] );

function contains (variable, arr) {
    arr.forEach(function (ar, index) {
        if (variable == ar)
            return true;
    });
}

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

var rooms = [
    [3,0],[8,0],[5, 2]
];

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

            
            if ( (x == 0 && y == 3) || (x == 11 && y == 3)) {
                var material = new THREE.MeshPhongMaterial( {
                    color: 0x00ff00,
                    emissive: 0x072534,
                    shading: THREE.FlatShading
                } );
                var cube = new THREE.Mesh( geometry, material );
            } else if (isBoundary(x, y)) {
                var material = new THREE.MeshPhongMaterial( {
                    color: 0x808080,
                    shading: THREE.FlatShading
                } );
                var cube = new THREE.Mesh( geometry, material );
            } else if (isRoom(x, y)) {
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

var counter = 0;
var path = [
    [3, 1], [2, 1], [1, 1], [0, 1], [0, 2]
];

var pathway = new THREE.Mesh(
    new THREE.BoxGeometry(1, 1, 1),
    new THREE.MeshPhongMaterial({
        color: 0xff0000,
    })
);

function showPathWay() {
    scene.remove(pathway);
    pathway.position.x = path[Math.floor(counter)][0] - 6;
    pathway.position.y = path[Math.floor(counter)][1] - 2;
    scene.add(pathway);
    
    if (counter < path.length-.1)
        counter+=.1
    else
        counter = 0;
}

function requestDangerBlock() {
    $.ajax({
        url: 'http://localhost:5000/',
        type: 'GET',
        data: '', // or $('#myform').serializeArray()
        success: function(data) { alert(data); }
    });
}

render();