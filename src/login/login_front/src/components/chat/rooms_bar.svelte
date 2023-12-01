<script>
    import Room from "./room.svelte";

    export let rooms;
    
</script>


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
        /* padding: 1em;
        width: 10vw; */
        display:flex;
        flex-direction: column;
    }
</style>