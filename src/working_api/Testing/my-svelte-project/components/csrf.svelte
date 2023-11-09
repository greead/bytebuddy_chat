<script>
    import { csrf } from './store'

    async function handleCsrf(event) {
        let res = await fetch("http://localhost:8000/api/csrf/", {
            credentials: "include",
        })

        csrf.set(res.headers.get("X-CSRFToken"))
        console.log($csrf)
    }
    
</script>

<button on:click={handleCsrf}>CSRF</button>