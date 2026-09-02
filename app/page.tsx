// pages/index.js (or pages/index.tsx if you are using TypeScript)
import Image from 'next/image';
import * as React from 'react';
import Link from 'next/link';

export default function Home() {
  return (
    <section>
      <main>
        <div className="max-w-4xl mx-auto sm:pt-16 text-center">
          <h1 className="text-4xl sm:text-6xl font-medium mx-auto pb-6 tracking-tighter">
            Your
            <span className="text-yellow-600"> American Sign Language</span>
            <span className="block font-medium"> Journey Begins Here</span>
          </h1>
          <p className="mb-4 text-xl">Our curriculum is free and open source</p>
          <div className="pb-8 max-w-xl mx-auto">
            <Link href="/lessons">
              <button className="h-10 px-5 text-yellow-600 transition-colors duration-150 border border-yellow-600 rounded-lg focus:shadow-outline hover:bg-yellow-600 hover:text-yellow-100">Browse Lessons</button>
            </Link>
          </div>
        </div>

        <Image
          src="/Images/logoBW.png"
          alt="Image"
          width="0"
          height="0"
          sizes="fit"
          className="w-full h-auto"
        />
      </main>
    </section>
  );
}
