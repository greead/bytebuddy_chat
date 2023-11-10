import { writable } from 'svelte/store';

export const csrf = writable('');

export const auth = writable(false);

export const sessionid = writable('');

export const username = writable('');

export const password = writable('')

export const data = writable()

export const page = writable('login')

export async function handleCsrf(event) {
    let res = await fetch("http://localhost:8000/csrf/", {
        credentials: "include",
    })

    csrf.set(res.headers.get("X-CSRFToken"))
}