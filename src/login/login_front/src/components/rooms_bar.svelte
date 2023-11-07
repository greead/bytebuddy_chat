<script>
    import Room from "./room.svelte";

    let rooms = ['Room1', 'Room2']
</script>


<div >
    <p>Rooms</p>
    {#each rooms as room}
        <Room text={room}/>
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