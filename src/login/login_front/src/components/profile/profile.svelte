<script>
    import Nav from "../navbar/nav.svelte"
    import {displayName, bio,userid, csrf, handleCsrf, img} from "../store"
    console.log($userid)
    import { onMount } from 'svelte';

    const basicProfile = 'media/images/basicProfile.png'
    onMount(() => {
        getPfp()
    });

    let isEditable = false;
    let avatar;

    // async function getPfp(event) {
    //     await handleCsrf()
    //     // console.log($csrf)
    //     // console.log('csrftoken:', $csrf)
    //     console.log($userid)
    //     let res = await fetch("http://localhost:8000/profilePicture/", {
    //         method: "POST",
    //         headers: {
    //             "Content-Type": "application/json",
    //             "X-CSRFToken": $csrf,
    //         },
    //         credentials: "include",
    //         body: JSON.stringify({userid: $userid}),
    // })

    //     let dat = await res.json()
    //     // console.log(dat)
    //     // if ('image_url' in data) {
    //         dat.image_url = dat.image_url.replace('/media', '../../../../../media');
    //     // }
    //     console.log(dat)
    // }

    async function getPfp(event) {
        const res = await fetch(`http://localhost:8000/profile?userid=${$userid}`);

        let dat = await res.json()
        //url returned is /image/xxx.jpeg and svelte will only search in the public folder --> need 
        avatar = dat.image_url;
        console.log(avatar)
    }

    function toggleEditable() {
      isEditable = true;
    }

    async function handleSubmit() {
      // Add your form submission logic her
      console.log('Form submitted!');
      isEditable = false; // After submission, make the form non-editable again

      // let binaryString = String.fromCharCode.apply(null, new Uint8Array($img));
      // let base64Data = btoa(binaryString);

      const formData = new FormData();
      formData.append('userid',$userid)
      formData.append('image', $img);
      formData.append('bio', $bio);
      formData.append('display_name', $displayName);
      // console.log($displayName)
      // console.log($bio)
      // console.log($img)
    
      await handleCsrf()
        // console.log($csrf)
        // console.log('csrftoken:', $csrf)
        // console.log($userid)
        let res = await fetch("http://localhost:8000/chat/image/", {
            method: "POST",
            headers: {
                "X-CSRFToken": $csrf,
            },
            credentials: "include",
            body: formData,
    })
    }

    function handleFileInputChange(event) {
        const fileInput = event.target;
        let image = fileInput.files[0];
        // console.log($img)

        // console.log(selectedFile)
        let reader = new FileReader();
        reader.onload = function (e) {
        // Set the source of the image to the data URL obtained from FileReader
            img.set(String(e.target.result));
            avatar = e.target.result;
            // console.log($img)xs
      };
            reader.readAsDataURL(image);
  }

</script>

<Nav />

<!-- To-do: need to add a box for profile picture and position things around -->
<div id= "full-page">
  
    <!-- <img id="avatar" src={"http://localhost:5173/" + avatar} alt="img"> -->
 
    <!-- {#if avatar} -->
      <img id="avatar" class="flex-item" src={avatar} alt="Profile">
    <!-- {:else} -->
      <!-- <img id="avatar" class="flex-item" src={"http://localhost:5173/" + basicProfile} alt="Profile"> -->
    <!-- {/if} -->
    
    <!-- <form on:submit|preventDefault={handleSubmit} class="flex-item"> -->
    <div class="form flex-item">
      <!-- Your form fields go here -->
      <div class="form-inside">
        <lable for="displayName">Alias </lable>
        <input bind:value={$displayName} type="text" id="displayName" name="displayName" style="input_item" disabled= { !isEditable}>
    </div>
   
      
      <div class="form-inside">
        <!-- <lable for="bio">Bio</lable>
        <textarea bind:value={$bio} id="bio" name="bio" disabled= { !isEditable}></textarea> -->
      </div>

      <div class="form-inside file-upload-box">
            <lable>Avatar</lable>
            <input class="choose_file" type="file" id="fileInput" accept=".png, .jpg, .jpeg" on:change={handleFileInputChange} disabled= { !isEditable}/>
            <!-- <span class="file-upload-label">{selectedFile ? selectedFile.name : 'No file chosen'}</span> -->
      </div>
      {#if isEditable}
        <button on:click={handleSubmit}>Submit</button>
      {:else}
        <button on:click={toggleEditable}>Edit</button>
      {/if}
    <!-- </form> -->
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
        /* margin:3vw; */
        margin-top: 2vw;
        margin-bottom: 1vw;
        /* height:20vw; */
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

    lable{
      border: 2 em;
      border-color: black;
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
  lable{
      color:white;
      padding-left:5%;
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

    textarea{
        padding-left: 1.1%;
        font-family: 'VT323';
        width: 18vw;
        height: 10vw;
        font-size: 0.75em;
        resize: horizontal;
        line-height: 1;
        overflow-x: scroll;
        margin-right:5%;
        border-radius:.3em;
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