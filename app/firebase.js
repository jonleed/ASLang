// Import the functions you need from the SDKs you need
import { getApp, getApps, initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getDatabase, ref, set } from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries


// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
  databaseURL: "https://aslang-b56b7-default-rtdb.firebaseio.com"
};

const isFirebaseConfigured = Object.entries(firebaseConfig)
  .filter(([key]) => key !== "databaseURL")
  .every(([, value]) => Boolean(value));

// Keep the app browseable when the original Firebase credentials are unavailable.
const app = isFirebaseConfigured
  ? (getApps().length ? getApp() : initializeApp(firebaseConfig))
  : null;

// Initialize Realtime Database and get a reference to the service
export const auth = app ? getAuth(app) : null;
export const db = app ? getDatabase(app) : null;

export function writeUserData(userId, completed) {
    if (!db) {
      throw new Error("Firebase is not configured. Add the NEXT_PUBLIC_FIREBASE_* values to .env.local.");
    }

    const reference = ref(db, 'users/' + userId);

    set(reference, {
      numDone: completed
    });
}
