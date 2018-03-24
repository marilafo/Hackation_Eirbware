import React, {Component} from 'react';
import { StyleSheet, Text, View } from 'react-native';
import StartButton from '../elements/buttons/StartButton';

export default class Home extends Component {
  static navigationOptions = {
    header: null,
  }

  render() {
    return (
      <View style={styles.button}>
        <View style={{flex: 1}} />
        <StartButton
          onPress = {() => console.log('pressed !')}
          />
        <View style={{flex: 1}} />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  button: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
