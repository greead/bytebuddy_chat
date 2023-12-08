<script> // Users bar Svelte component
    import User from "./user.svelte";
    export let users;
</script>

<!-- Users bar contents -->
<div >
    <p>Active Users</p>
    {#each users as user}
        <User display_name={user.user} profile_picture={user.image}/>
    {/each}
</div>

<style>
    p {
        color: white;
    }
    div {
        width: 10vw;
    }
</style>