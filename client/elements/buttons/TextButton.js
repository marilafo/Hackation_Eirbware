import React, {Component} from 'react';
import { TouchableHighlight, Text, View, StyleSheet } from 'react-native';
import { MaterialIcons as Icon } from '@expo/vector-icons';

export default class TextButton extends Component{

  render(){
    return(
      <View style={{flex:3}}>
        <TouchableHighlight
          underlayColor="#4189fc"
          onPress={this.props.onPress}
          style={styles.circleButton}>
            <Text style={styles.text}>{this.props.text}</Text>
        </TouchableHighlight>
    </View>
    );
  }
}
const styles = StyleSheet.create({
  circleButton: {
    alignItems:'center',
    justifyContent:'center',
    backgroundColor:'#1c73ff',
    borderRadius:50,
    height: 70,
  },
  text: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff'
  },
})
