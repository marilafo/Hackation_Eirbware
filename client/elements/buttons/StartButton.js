import React, {Component} from 'react';
import { TouchableHighlight, Text, View, StyleSheet } from 'react-native';
import { MaterialIcons as Icon } from '@expo/vector-icons';

export default class StartButton extends Component{

  render(){
    return(
      <View style={{flex:8}}>
        <TouchableHighlight
          underlayColor="#4189fc"
          onPress={this.props.onPress}
          style={styles.circleButton}>
            <Text style={styles.text}>Start</Text>
        </TouchableHighlight>
    </View>
    );
  }
}
const styles = StyleSheet.create({
  circleButton: {
    alignItems:'center',
    justifyContent:'center',
    backgroundColor:'#fff',
    borderRadius:50,
    height: 100,
  },
  text: {
    fontSize: 40,
    fontWeight: 'bold',
    color: '#1c73ff'
  },
})
