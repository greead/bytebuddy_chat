<script>
    import Room from "./room.svelte";

    let rooms = ['Dummy']
    
</script>


<div >
    <p>Rooms</p>
    {#each rooms as room}
        <Room roomName={room}/>
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