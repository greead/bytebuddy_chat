<script>
    // export let pfp = "https://static.vecteezy.com/system/resources/previews/020/765/399/non_2x/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg"
    // export let pfp = 'media/images/basicProfile.png'
    // import basicProfile from '/images/basicProfile.png'

    export let display_name = "User";
    export let profile_picture = "http://localhost:5173/media/images/basicProfile.png";
    // import basicProfile from '/media/images/basicProfile.png'
</script>

<div>
    <img src={"http://localhost:5173/" + profile_picture} alt="img"><span>{display_name}</span>
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
        /* padding-left: 4px; */
        padding-bottom: 0.75em;
    }

    span {
        /* padding-left: 4px; */
        color: rgb(255, 255, 255);
        font-family: 'VT323';
    }

</style>