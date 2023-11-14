<script>
    import User from "./user.svelte";

    export let users;
</script>

<div >
    <p>Active Users</p>
    {#each users as user}
        <User name={user}/>
    {/each}
</div>

<style>
    p {
        color: white;
    }
    div {
        padding: 8px;
        width: 10vw;
    }
</style>