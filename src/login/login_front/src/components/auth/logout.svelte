<script>
    import { navigate } from 'svelte-routing';
    import { data } from '../store'

    async function handleLogout(event) {
        let res = await fetch("http://localhost:8000/logout/", {
            credentials: "include",
        })

        data.set(await res.json())
        console.log($data)

        if (res.ok) {
            navigate('/')
        }
    }
    
</script>

<button on:click={handleLogout}>Logout</button>
