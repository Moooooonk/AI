import React, { useState, useEffect } from 'react';
import { View, Button, StyleSheet } from 'react-native';
import { Audio } from 'expo-av';
import { GLView } from 'expo-gl';
import * as THREE from 'three';

export default function App() {
    const [sound, setSound] = useState();
    const [isPlaying, setIsPlaying] = useState(false);

    async function loadSound() {
        const { sound } = await Audio.Sound.createAsync(require('./assets/sample-audio.mp3'));
        setSound(sound);
        await sound.playAsync();
        setIsPlaying(true);
    }

    function renderScene(gl) {
        const renderer = new THREE.WebGLRenderer({ canvas: gl });
        renderer.setSize(gl.drawingBufferWidth, gl.drawingBufferHeight);
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, gl.drawingBufferWidth / gl.drawingBufferHeight, 0.1, 1000);
        camera.position.z = 5;

        const geometry = new THREE.SphereGeometry(1, 32, 32);
        const material = new THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: true });
        const sphere = new THREE.Mesh(geometry, material);
        scene.add(sphere);

        const animate = () => {
            requestAnimationFrame(animate);
            if (isPlaying) {
                const scaleValue = Math.sin(Date.now() * 0.001) + 2;  // 임의의 크기 조정
                sphere.scale.set(scaleValue, scaleValue, scaleValue);
            }
            renderer.render(scene, camera);
            gl.endFrameEXP();
        };
        animate();
    }

    return (
        <View style={styles.container}>
            <Button title="Play Sound" onPress={loadSound} />
            <GLView style={styles.glView} onContextCreate={renderScene} />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#000'
    },
    glView: {
        width: '100%',
        height: '80%',
    }
});
