<script>
    export let name = "User";
    export let pfp = "https://static.vecteezy.com/system/resources/previews/020/765/399/non_2x/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg"
</script>

<div>
    <img src={pfp} alt="pfp"><span>{name}</span>
</div>

<style>
    img {
        width: 2em;
        height: 2em;
    }

    div {
        display: flex;
        justify-content: left;
        align-items: center;
        width: 100%;
        padding-left: 4px;
        padding-bottom: 4px;
    }

    span {
        padding-left: 4px;
        color: rgb(255, 255, 255);
    }

</style>