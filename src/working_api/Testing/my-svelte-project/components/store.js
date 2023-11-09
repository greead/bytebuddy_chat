import { writable } from 'svelte/store';

export const csrf = writable('');

export const auth = writable(false);

export const sessionid = writable('');

export const username = writable('');

export const password = writable('')

export const data = writable()

export const page = writable('login')