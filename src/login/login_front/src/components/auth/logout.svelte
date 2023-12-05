<script>
    import { navigate } from 'svelte-routing';

    async function handleLogout(event) {
        let res = await fetch("http://localhost:8000/logout/", {
            credentials: "include",
        })

        if (res.ok) {
            navigate('/')
        }
    }
    
</script>

<button on:click={handleLogout}>Logout</button>
