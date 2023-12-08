<script> // Profile page Svelte component
    import Nav from "../navbar/nav.svelte"
    import {displayName, bio,userid, csrf, handleCsrf, img} from "../store"
    console.log($userid)
    import { onMount } from 'svelte';

    const basicProfile = 'media/images/basicProfile.png'

    // Get the user's profile picture when the component is mounted.
    onMount(() => {
        getPfp()
    });

    let isEditable = false;
    let avatar;

    /**
     * Event handler to fetch the user's profile picture.
     * @param event The event caller.
     */
    async function getPfp(event) {
        const res = await fetch(`http://localhost:8000/profile?userid=${$userid}`);

        let dat = await res.json()
        avatar = dat.image_url;
        $displayName = dat.alias;
    }

    /**
     * Function to toggle the components on.
     */
    function toggleEditable() {
      isEditable = true;
    }

    /**
     * Event handler to submit the user's changes to their profile.
     */
    async function handleSubmit() {
      console.log('Form submitted!');
      isEditable = false;

      const formData = new FormData();
      formData.append('userid',$userid)
      formData.append('image', $img);
      formData.append('bio', $bio);
      formData.append('display_name', $displayName);
    
      await handleCsrf()
      let res = await fetch("http://localhost:8000/chat/image/", {
          method: "POST",
          headers: {
              "X-CSRFToken": $csrf,
          },
          credentials: "include",
          body: formData,
      })
    }

    /**
     * Event handler to handler a user attempting to add a new image to their profile.
     * @param event The event caller.
     */
    function handleFileInputChange(event) {
        const fileInput = event.target;
        let image = fileInput.files[0];

        let reader = new FileReader();
        reader.onload = function (e) {
        // Set the source of the image to the data URL obtained from FileReader
            img.set(String(e.target.result));
            avatar = e.target.result;
      };
            reader.readAsDataURL(image);
  }

</script>

<!-- Profile page contents -->
<Nav />

<!-- Profile editing form -->
<div id= "full-page">
    <img id="avatar" class="flex-item" src={avatar} alt="Profile">
    <div class="form flex-item">
      <div class="form-inside">
        <label for="displayName">Alias </label>
        <input bind:value={$displayName} type="text" id="displayName" name="displayName" style="input_item" disabled= { !isEditable}>
      </div>
      <div class="form-inside">
      </div>
      <div class="form-inside file-upload-box">
            <label for="fileInput">Avatar</label>
            <input class="choose_file" type="file" id="fileInput" accept=".png, .jpg, .jpeg" on:change={handleFileInputChange} disabled= { !isEditable}/>
      </div>
      {#if isEditable}
        <button on:click={handleSubmit}>Submit</button>
      {:else}
        <button on:click={toggleEditable}>Edit</button>
      {/if}
    </div>
</div>

<style>
    #full-page{
        display:flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        width:100%;
        height:50vw;
    }

    img{
        object-fit: cover;
        width: 20%; /* Ensure the image takes 100% of the container width */
        height: 40%;
        border-radius: 1em;
        }

    .flex-item{
        margin-top: 2vw;
        margin-bottom: 1vw;
    }

    .choose_file {
        height: max-content;
    }

    .form{
        width: 30%;
        display:flex;
        flex-direction:column;
        align-items: center;
        justify-content: space-evenly;
        font-family: 'VT323';
    }

    label{
      border: 2 em;
      border-color: black;
      color:white;
      padding-left:5%;
    }

    .form-inside{
        width:100%;
        display:flex;
        flex-direction:row;
        align-items: center;
        justify-content:space-between;
        font-family: 'VT323';
        color:white;
        font-size:2em;
    }

    input{
        font-family: 'VT323';
        width: 18vw;
        height: 1.5vw;
        font-size: 0.75em;
        margin-right:5%;
        border-radius:.3em;
        padding-left: 1.1%;
    }
    
    #fileInput{
    
      font-size: 0.5em;
      padding-right: 0.5em;
    }

    button{
        margin-top: 1em;
        width: 30%;
    }
</style>