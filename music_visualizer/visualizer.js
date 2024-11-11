let audio, audioContext, analyser, dataArray;
const canvas = document.createElement('canvas');
document.body.appendChild(canvas);
const renderer = new THREE.WebGLRenderer({ canvas });
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 10;

// 3D 오브젝트 생성
const spheres = [];
for (let i = 0; i < 20; i++) {
    const geometry = new THREE.SphereGeometry(0.5, 32, 32);
    const material = new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0x112244, metalness: 0.6 });
    const sphere = new THREE.Mesh(geometry, material);
    sphere.position.x = Math.random() * 20 - 10;
    sphere.position.y = Math.random() * 10 - 5;
    sphere.position.z = Math.random() * 10 - 5;
    spheres.push(sphere);
    scene.add(sphere);
}

const ambientLight = new THREE.AmbientLight(0x404040, 1);
scene.add(ambientLight);
const pointLight = new THREE.PointLight(0xaaaaaa, 1);
pointLight.position.set(0, 5, 10);
scene.add(pointLight);

document.getElementById('audioFile').addEventListener('change', function(e) {
    const file = e.target.files[0];
    audio = new Audio(URL.createObjectURL(file));
    audioContext = new AudioContext();
    const source = audioContext.createMediaElementSource(audio);
    analyser = audioContext.createAnalyser();
    source.connect(analyser);
    analyser.connect(audioContext.destination);
    analyser.fftSize = 256;
    dataArray = new Uint8Array(analyser.frequencyBinCount);
    audio.play();
    animate();
});

function animate() {
    requestAnimationFrame(animate);
    analyser.getByteFrequencyData(dataArray);

    spheres.forEach((sphere, i) => {
        const scale = (dataArray[i] / 128.0) + 0.5;
        sphere.scale.set(scale, scale, scale);

        const colorFactor = dataArray[i] / 255;
        sphere.material.emissive.setHSL(colorFactor, 0.7, 0.5);
    });

    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.render(scene, camera);
}
