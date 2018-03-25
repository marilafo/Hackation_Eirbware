import React, {Component} from 'react';
import { ActivityIndicator, StyleSheet, Text, View } from 'react-native';


export default class Wait extends Component {
  static navigationOptions = {
    header: null,
  }

  state = {
    isLoading: true,
  }

  componentDidMount() {
    let socket =  this.props.navigation.state.params.socket;
    socket.on('wyr_ask', (data) => {
      let json = data.json();
    })
  }

  render() {
    if(this.state.isLoading){
      return(
        <View style={{flex: 1, padding: 20}}>
          <ActivityIndicator/>
        </View>
      )
    }

    return (
      <View>
      </View>
    );
  }
}
