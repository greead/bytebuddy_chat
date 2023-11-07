/**
 * Svelte store for shared/stored information
 */
import { writable } from "svelte/store";

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

/**
 * Svelte store item for ChatConsumer WebSocket
 */
let sock = null;
const openSocket = (socketURL) => {
    sock.close()
    const socket = new WebSocket(socketURL)

    // Connection opened
    socket.addEventListener('open', function (event) {
        console.log("It's open");
    });

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