import React from 'react';
import { withGoogleMap, GoogleMap, Marker } from 'react-google-maps';

const googleMapURL="https://maps.googleapis.com/maps/api/js?v=3.27&libraries=places,geometry&key=AIzaSyBMc_L847oGm0yvye5IsYGyQnfWGs1ryq4";

const GoogleMapComponent = withGoogleMap(props => (
    <GoogleMap
        ref={props.onMapLoad}
        defaultZoom={8}
        defaultCenter={{ lat: -25, lng: 131 }}
        googleMapURL={googleMapURL}
        onClick={props.onMapClick}
    />
));

class MapBackground extends React.Component {
    render() {
        return (
        <div className='mapBg' >
            <GoogleMapComponent
                containerElement={ <div style={{ height: '100%' }}/> }
                mapElement={ <div style={{ height: '100%' }}/> }
            />
        </div>);
    }
}

export default MapBackground;
