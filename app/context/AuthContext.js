"use client";

import { useContext, createContext, useState, useEffect } from "react";
import { signInWithPopup, signOut, onAuthStateChanged, GoogleAuthProvider } from "firebase/auth";
import { auth, writeUserData } from "../firebase";

const AuthContext  = createContext();

export const AuthContextProvider = ({children}) => {
    const [user, setUser] = useState(null);

    const googleSignIn = async () => {
        if (!auth) {
            throw new Error("Firebase is not configured. Add the NEXT_PUBLIC_FIREBASE_* values to .env.local.");
        }

        const provider = new GoogleAuthProvider;
        try {
            const result = await signInWithPopup(auth, provider);
            // This gives you a Google Access Token. You can use it to access the Google API.
            // The signed-in user info.
            const user = result.user;

            writeUserData(user.uid, 0);
        } catch (error) {
            console.error("Google sign-in failed", error);
            throw error;
        }
    }

    const logOut = () => {
        if (auth) {
            return signOut(auth);
        }
    }

    useEffect(() => {
        if (!auth) {
            return;
        }

        const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
            setUser(currentUser);
        })

        return () => unsubscribe;
    }, [])

    return (
        <AuthContext.Provider value={{ user, googleSignIn, logOut }}>
            {children}
        </AuthContext.Provider>
    )
}

export const UserAuth = () => {
    return useContext(AuthContext);
}
