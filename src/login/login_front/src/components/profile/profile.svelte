<script>
    import Nav from "../navbar/nav.svelte"
    import {displayName, bio,userid, csrf} from "../store"
    console.log($userid)
    import { onMount } from 'svelte';
    import basicProfile from '../../../../../media/images/basicProfile.png'
    onMount(() => {
        getPfp()
    });

    // To-do:
    // views and urls are alreaday set up to return a url in json format
    // need to figure out a way to send post request to backend server
    // right now, if I refresh page, userID, sessionID and CSRF are also reset
    // so, I couldn't use them. Also, since we have sessionID, should we use it instead of CSRF
    async function getPfp(event) {
        let res = await fetch("http://localhost:8000/profilePicture/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf,
            },
            credentials: "include",
            body: JSON.stringify({userid: $userid}),
    })

        let dat = await res.json()
        console.log(dat)
    }

    let isEditable = false;

    function toggleEditable() {
      isEditable = true;
    }

    function handleSubmit() {
      // Add your form submission logic here
      selectedFile = input.files[0];
        console.log(selectedFile);
      console.log('Form submitted!');
      isEditable = false; // After submission, make the form non-editable again
    }

    let selectedFile;
    let input;
    function handleFileInputChange() {
        const imagePreview = document.getElementById('avatar');
        selectedFile = input.files[0];
        console.log(selectedFile)
        let reader = new FileReader();
        reader.onload = function (e) {
        // Set the source of the image to the data URL obtained from FileReader
            imagePreview.src = e.target.result;
      };
            reader.readAsDataURL(selectedFile);
  }

</script>

<Nav />

<!-- To-do: need to add a box for profile picture and position things around -->
<div id= "full-page">
    <img id="avatar" class="flex-item" src={basicProfile} alt="Profile" width="20%">
    <form on:submit|preventDefault={handleSubmit} class="flex-item">
      <!-- Your form fields go here -->
      <div class="form-inside">
        <lable for="displayName">DisplayName </lable>
        <input bind:value={$displayName} type="text" id="displayName" name="displayName" style="input_item" disabled= { !isEditable}>
    </div>
   
      
      <div class="form-inside" disabled= { !isEditable}>
        <lable for="bio">Bio</lable>
        <textarea bind:value={$bio} id="bio" name="bio" disabled= { !isEditable}></textarea>
     </div>

      <div class="form-inside file-upload-box">
            <lable>Avatar</lable>
            <input type="file" id="fileInput" accept=".png, .jpg, .jpeg" on:change={handleFileInputChange} disabled= { !isEditable} bind:value={input}/>
            <!-- <span class="file-upload-label">{selectedFile ? selectedFile.name : 'No file chosen'}</span> -->
      </div>
      {#if isEditable}
        <button type="submit">Submit</button>
      {:else}
        <button on:click={toggleEditable}>Edit</button>
      {/if}
    </form>
    
    
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

    .flex-item{
        /* margin:3vw; */
        margin-bottom: 3vw;
        height:20vw;
    }

    form{
        width: 30%;
        display:flex;
        flex-direction:column;
        align-items: center;
        justify-content: space-evenly;
        font-family: 'VT323';
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
        padding: 1 em;
    }

    textarea{
        padding: 0.15em;
        font-family: 'VT323';
        width: 18vw;
        height: 10vw;
        font-size: 0.75em;
        resize: horizontal;
        line-height: 1;
        overflow-x: scroll;
}
    #fileInput{
    
      font-size: 0.5em;
      padding-right: 0.5em;
      /* right: 0;
      top: 0; */
    }

    button{
        margin-top: 1em;
        width: 30%;
    }
</style>