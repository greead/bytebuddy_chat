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