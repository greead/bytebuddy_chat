<script>
    import { csrf, username, password, data, page } from './store'

    async function handleLogin(event) {
        let res = await fetch("http://localhost:8000/api/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf,
            },
            credentials: "include",
            body: JSON.stringify({username: $username, password: $password}),
        })

        console.log(res.ok)
        data.set(await res.text())
        page.set('logout')
    }
    
</script>

<input type="text" bind:value={$username}/><br>
<input type="text" bind:value={$password}/><br>

<button on:click={handleLogin}>Login</button>