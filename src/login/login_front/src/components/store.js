import { writable, derived } from 'svelte/store';

// AUTH STORE //
export const csrf = writable('');

export const auth = writable(false);

export const sessionid = writable('');

export const username = writable('');

export const password = writable('')

export const data = writable()

// export const userid = writable('')
export const userid = writable(localStorage.getItem("userid") || "");
userid.subscribe(val => localStorage.setItem("userid", val));

//Kole: is this my work?
// function getStoredUser() {
//   const storedUser = localStorage.getItem('userid');
//   return storedUser ? JSON.parse(storedUser) : { id: null, username: null };
// }

export const displayName = writable('')

export const bio= writable('')

export const img= writable('')

export const current_room = writable('')

export async function handleCsrf(event) {
    let res = await fetch("http://localhost:8000/csrf/", {
        credentials: "include",
    })

    csrf.set(res.headers.get("X-CSRFToken"))
}
// AUTH STORE //

// CHAT STORE //
export const uri = writable('')

export const uri_ide = writable('')

let ide_previous = ''

export const ide_contents = writable('')

export const isUnchanged = derived(ide_contents, ($ide_contents) => $ide_contents === ide_previous)

export const user_store = writable([])

export const message_list = writable([])

function createWebSocketStore(url) {
  const { subscribe, set, update } = writable({
    websocket: null,
    message: '',
    isConnected: false,
  });

  let ws;

  const connectWebSocket = () => {
    user_store.set([])
    ws = new WebSocket(url);

    ws.onopen = () => {
      update((state) => ({ ...state, websocket: ws, isConnected: true }));
      console.log('WebSocket opened at:', url);
    };

    ws.onmessage = (event) => {
      // update((state) => ({ ...state, message: event.data }));
      // console.log('WebSocket message received:', event.data)
      const data = JSON.parse(event.data);
      console.log(data);
      switch (data.type) {
        case "chat_message":
          message_list.update((list) => ([...list, {user:data.user, content:data.message}]))
          // update((state) => ({ ...state, message: data.user + ": " + data.message }));
          break;
        case "message_list":
          message_list.set(data.message)
          break;
        case "user_list":
          user_store.set(data.users);
          break;
        case "user_join":
          message_list.update((list) => ([...list, {user:data.user, content:data.message, sys:true}]))
          break;
        case "user_leave":
          message_list.update((list) => ([...list, {user:data.user, content:data.message, sys:true}]))
          break;     
        default:
          console.error("Unknown message type!");
          break;
      }
    };

    ws.onclose = () => {
      update((state) => ({ ...state, websocket: null, isConnected: false }));
      console.log('WebSocket closed at:', url)
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    

  };

  const disconnectWebSocket = () => {
    if (ws) {
      ws.close();
    }
  };

  const sendMessage = (msg) => {
    if(ws) {
        ws.send(JSON.stringify({
          "message":msg
        }));
        console.log('WebSocket message sent:', msg)
    }
  };

  return {
    subscribe,
    connectWebSocket,
    disconnectWebSocket,
    sendMessage,
  };
};

function createIDESocketStore(url) {
  const { subscribe, set, update } = writable({
    websocket: null,
    isConnected: false,
  });

  let ws;

  const connectWebSocket = () => {
    ws = new WebSocket(url);

    ws.onopen = () => {
      update((state) => ({ ...state, websocket: ws, isConnected: true }));
      console.log('WebSocket opened at:', url);
    };

    ws.onmessage = (event) => {
      // update((state) => ({ ...state, message: event.data }));
      // console.log('WebSocket message received:', event.data)
      const data = JSON.parse(event.data);
      console.log(data);
      if (data.type === "ide_message") {
        ide_contents.set(data.message)
        ide_previous = data.message
      }
    };

    ws.onclose = () => {
      update((state) => ({ ...state, websocket: null, isConnected: false }));
      console.log('WebSocket closed at:', url)
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  };

  const disconnectWebSocket = () => {
    if (ws) {
      ws.close();
    }
  };

  const sendMessage = (msg) => {
    if(ws.readyState === ws.OPEN) {
        ws.send(JSON.stringify({
          "message":msg
        }));
        console.log('WebSocket message sent:', msg)
    }
  };

  return {
    subscribe,
    connectWebSocket,
    disconnectWebSocket,
    sendMessage,
  };
};

export const wss = derived(uri, ($uri) => createWebSocketStore($uri));
export const wss_ide = derived(uri_ide, ($uri_ide) => createIDESocketStore($uri_ide))

// CHAT STORE //

