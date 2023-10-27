import { writable } from "svelte/store";

export const user = writable({
    email:"testing@pfw.edu",
    password:"123456",
})