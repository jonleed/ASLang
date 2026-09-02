import { auth, db, writeUserData } from '@/app/firebase';
import { onValue, ref } from 'firebase/database';


let userId;
if(auth?.currentUser && db) {
  userId = auth.currentUser.uid;
  if(!ref(db, 'users/' + userId))
    writeUserData(userId, 0);
} else {
  // Do toast message for user to log in
}

let numDone = 0;

if(userId && db) {
  const numDoneRef = ref(db, 'users/' + userId + '/numDone') 
  onValue(numDoneRef, (snapshop) => {
    const data = snapshop.val();
    numDone = +data;
  })
}

const GetCompletion = (lessonNum: number) => {
  if(numDone > lessonNum) {
    <div className="p-8 border-gray-200 dark:border-gray-600">
      <div className="flex justify-between rounded-lg shadow-xl ring-1 ring-black ring-opacity-5 mx-auto p-10 w-2/3">
        <div className="my-auto">Lesson</div>
      <div><button className="h-12 px-12 m-auto text-white transition-colors duration-150 bg-green-700 rounded-lg focus:shadow-outline hover:bg-green-800">Completed</button></div>
    </div>
    </div>
  } else if(numDone === lessonNum) {
    <div className="p-8 border-gray-200 dark:border-gray-600">
      <div className="flex justify-between rounded-lg shadow-xl ring-1 ring-black ring-opacity-5 mx-auto p-10 w-2/3">
        <div className="my-auto">Lesson</div>
      <div><button className="h-12 px-12 m-auto text-white transition-colors duration-150 bg-indigo-700 rounded-lg focus:shadow-outline hover:bg-indigo-800">Begin</button></div>
    </div>
    </div>
  } else {  // numDone < lessonNum
    <div className="p-8 border-gray-200 dark:border-gray-600">
      <div className="flex justify-between rounded-lg shadow-xl ring-1 ring-black ring-opacity-5 mx-auto p-10 w-2/3">
        <div className="my-auto">Lesson</div>
      <div><button className="h-12 px-12 m-auto text-white transition-colors duration-150 bg-zinc-500 rounded-lg focus:shadow-outline hover:bg-zinc-600"></button></div>
    </div>
    </div>
  }
}



export default GetCompletion
