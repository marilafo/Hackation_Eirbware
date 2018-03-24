import React, {Component} from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default class Form extends Component {
  static navigationOptions = {
    header: null,
  }

  render(){
    return(
      <View style={{flex:1,backgroundColor: '#fff'}}>
        <View style={styles.placeTitle}>
          <Text style={styles.title}>Player</Text>
        </View>
      </View>
    );
  }
}
const styles = StyleSheet.create({
  placeTitle: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 40,
    fontWeight: 'bold',
    color: '#1c73ff',
  },
});
