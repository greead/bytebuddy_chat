<script>
    import User from "./user.svelte";

    let users = ['User1', 'User2']
</script>

<div >
    <p>Active Users</p>
    {#each users as user}
        <User text={user}/>
    {/each}
</div>

<style>
    p {
        color: white;
    }
    div {
        padding: 8px;
    }
</style>