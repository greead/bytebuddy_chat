<script> // Rooms bar Svelte component
    import Room from "./room.svelte";
    export let rooms;    
</script>

<!-- Rooms bar contents -->
<div >
    <p>Rooms</p>
    {#if rooms}
        {#each rooms as room}
            <Room roomName={room}/>
        {/each}
    {/if}
</div>

<style>
    p {
        color: white;
    }
    div {
        display:flex;
        flex-direction: column;
    }
</style>