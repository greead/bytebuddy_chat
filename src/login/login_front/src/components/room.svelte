<script>
    // import store from "./store";

    export let text = "Room";

    async function connectRoom() {
        // store.openSocket(text)
    }

</script>

<div>
    <button on:click={connectRoom}>{text}</button>
</div>

<style>
    div {
        display: grid;
    }
</style>