<script> // User item Svelte component
    export let display_name = "User";
    export let profile_picture = "http://localhost:5173/media/images/basicProfile.png";
</script>

<!-- User contents -->
<div>
    <img src={"http://localhost:5173/media" + profile_picture} alt="img"><span>{display_name}</span>
</div>

<style>
    img {
        width: 2em;
        height: 2em;
    }

    div {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;
        width: 100%;
        padding-bottom: 0.75em;
    }

    span {
        color: rgb(255, 255, 255);
        font-family: 'VT323';
    }

</style>