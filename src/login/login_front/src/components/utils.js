export async function login(user) {

    const response = await fetch('http://127.0.0.1:8000/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.cookie
        },
        body: JSON.stringify(user),
        credentials: "include",
    });
    if (response.ok) {
        return await response.text()
    } else {
        throw new Error('Login failed')
    }
}

export function cookies() {
    return document.cookie
}