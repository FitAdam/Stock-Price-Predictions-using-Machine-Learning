import React from 'react';
import LandingPage from '../../LandingPage';
import { homeObjOne, homeObjTwo, homeObjThree, homeObjFour } from './Data';


function Home() {
  return (
    <>
      <LandingPage {...homeObjOne} />
      <LandingPage {...homeObjThree} />
      <LandingPage {...homeObjTwo} />
    </>
  );
}

export default Home;