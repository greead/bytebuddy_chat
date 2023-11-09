/**
 * Svelte store for shared/stored information
 */
import { readable, writable } from "svelte/store";

/**
 * Svelte store item representing a user
 */
export const user = writable({
    email:"testing@pfw.edu",
    password:"123456",
})

/**
 * Svelte store item represeneting a user during signup
 */
export const signupUser = writable({
    email:"test@pfw.edu",
    password:"123456",
    confirmPw:"123456"
})

/**
 * Svelte store item for messages
 */
const messageStore = writable('')

export const csrftoken = writable('')
export const sessionid = writable('')

/**
 * Svelte store item for ChatConsumer WebSocket
 */
let sock = null;
const openSocket = (roomName) => {
    if (sock != null) {
        sock.close()
    }
    console.log("Connecting to: " + "ws://" + "127.0.0.1:8000" + "/ws/chat/" + roomName + "/")
    const socket = new WebSocket("ws://" + window.location.host + "/ws/chat/" + roomName + "/")

    // Connection opened
    socket.addEventListener('open', function (event) {
        console.log("Successfully connected to the WebSocket.");
    });

    // Connection closed
    socket.onclose = function(e) {
        console.log("WebSocket connection closed unexpectedly. Trying to reconnect in 2s...");
        setTimeout(function() {
            console.log("Reconnecting...");
            // TODO connect();
        }, 2000);
    };

    // Listen for messages
    socket.addEventListener('message', function (event) {
        messageStore.set(event.data);
    });
    sock = socket   
}

const sendMessage = (message) => {
    if (sock != null) {
        if (sock.readyState <= 1) {
            sock.send(message);
        }
    } else {
        console.log("Socket not opened")
    }
    
}

export default {
    subscribe: messageStore.subscribe,
    sendMessage, openSocket
}