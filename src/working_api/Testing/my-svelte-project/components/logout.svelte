<script>
    import { csrf, username, password, data} from './store'

    async function handleLogout(event) {
        let res = await fetch("http://localhost:8000/api/logout/", {
            credentials: "include",
        })

        data.set(await res.text())
    }
    
</script>

<button on:click={handleLogout}>Logout</button>