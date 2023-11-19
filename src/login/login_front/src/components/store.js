import { writable, derived } from 'svelte/store';

// AUTH STORE //
export const csrf = writable('');

export const auth = writable(false);

export const sessionid = writable('');

export const username = writable('');

export const password = writable('')

export const data = writable()

export const userid = writable('')

export const displayName = writable('')

export const bio= writable('')

export async function handleCsrf(event) {
    let res = await fetch("http://localhost:8000/csrf/", {
        credentials: "include",
    })

    csrf.set(res.headers.get("X-CSRFToken"))
}
// AUTH STORE //

// CHAT STORE //
export const uri = writable('')

function createWebSocketStore(url) {
  const { subscribe, set, update } = writable({
    websocket: null,
    message: '',
    // message_bundle: [],
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
      switch (data.type) {
        case "chat_message":
          update((state) => ({ ...state, message: data.user + ": " + data.message }));
          break;
        case "message_list":
          for (let msg of data.message) {
            update((state) => ({...state, message: msg.user + ": " + msg.content}))
          }
            
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

export const wss = derived(uri, ($uri) => createWebSocketStore($uri));

// CHAT STORE //

