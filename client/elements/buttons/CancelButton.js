import React, {Component} from 'react';
import { TouchableHighlight, Text, View, StyleSheet } from 'react-native';
import { MaterialIcons as Icon } from '@expo/vector-icons';

export default class CancelButton extends Component{

  render(){
    return(
      <View style={{flex:1}}>
        <TouchableHighlight
          underlayColor="#fff"
          onPress={this.props.onPress}
          style={styles.circleButton}>
            <Text style={styles.text}>Cancel</Text>
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
    height: 70,
  },
  text: {
    fontSize: 25,
    fontWeight: 'bold',
    color: '#1c73ff'
  },
})
