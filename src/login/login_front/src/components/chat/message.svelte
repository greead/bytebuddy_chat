<script>
    export let user;
    export let message;
    export let system = false;
</script>
{#if !system}
    <div>{user}: {message}</div>
{:else}
    <div class="system">{message}</div>
{/if}

<style>
    .system {
        font-style: italic;
        
    }
</style>