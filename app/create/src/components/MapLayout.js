import React from 'react';
import { withGoogleMap, GoogleMap, Marker, InfoWindow} from 'react-google-maps';
import AddObjectiveDialog from './AddObjectiveDialog';

const googleMapURL="https://maps.googleapis.com/maps/api/js?v=3.27&libraries=places,geometry&key=AIzaSyBMc_L847oGm0yvye5IsYGyQnfWGs1ryq4";

const GoogleMapComponent = withGoogleMap(props => (
    <GoogleMap
        ref={props.onMapLoad}
        defaultZoom={8}
        defaultCenter={{ lat: -25, lng: 131 }}
        googleMapURL={googleMapURL}
        onClick={props.onMapClick}>

        {props.markers.map(marker => (
            <Marker {...marker}>
                <InfoWindow>
                    <div> {marker.key} </div>
                </InfoWindow>
            </Marker>
        ))}

    </GoogleMap>
));

export default class MapLayout extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            markers: [],
            selectedLat: null,
            selectedLng: null,
        }
        this.handleMapClick = this.handleMapClick.bind(this);
    }

    handleMapClick(event){
        this.setState({
            markers: this.state.markers,
            selectedLat: event.latLng.lat(),
            selectedLng: event.latLng.lng(),
        });
    }

    render() {
        return (
        <div style = {{height: '100vh', width: '100%'}}>
            <GoogleMapComponent
                containerElement={ <div style={{ height: '100%' }}/> }
                mapElement={ <div style={{ height: '100%' }}/> }
                onMapClick = {this.handleMapClick}
                markers = {this.state.markers}
            />

            {this.state.selectedLat != null ? (<AddObjectiveDialog/>) : (<div></div>)}
        </div>
        );
    }
}
