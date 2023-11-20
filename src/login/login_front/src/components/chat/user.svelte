<script>
    export let name = "User";
    // export let pfp = "https://static.vecteezy.com/system/resources/previews/020/765/399/non_2x/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg"
    // export let pfp = 'media/images/basicProfile.png'
    import basicProfile from '../../../../../media/images/basicProfile.png'
    // import basicProfile from '/media/images/basicProfile.png'
</script>

<div>
    <!-- TO-DO: return api or chatroom consumer to return all users along with their profile picture url -->
    <img src={basicProfile} alt={basicProfile}><span>{name}</span>
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