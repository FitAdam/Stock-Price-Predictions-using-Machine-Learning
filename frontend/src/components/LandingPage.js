import React from 'react';
import './LandingPage.css';

function LandingPage({
  lightBg,
  topLine,
  lightText,
  lightTextDesc,
  headline,
  description,
  img,
  alt,
  imgStart
}) {
  return (
    <>
      <div
        className={lightBg ? 'home_core-section' : 'home_core-section darkBg'}
      >
        <div className='container'>
          <div
            className='row home_core-row'
            style={{
              display: 'flex',
              flexDirection: imgStart === 'start' ? 'row-reverse' : 'row'
            }}
          >
            <div className='col'>
              <div className='home_core-text-wrapper'>
                <div className='top-line'>{topLine}</div>
                <h1 className={lightText ? 'heading' : 'heading dark'}>
                  {headline}
                </h1>
                <p
                  className={
                    lightTextDesc
                      ? 'home_core-subtitle'
                      : 'home_core-subtitle dark'
                  }
                >
                  {description}
                </p>
              
              </div>
            </div>
            <div className='col'>
              <div className='home_core-img-wrapper'>
                <img src={img} alt={alt} className='home_core-img' />
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default LandingPage;