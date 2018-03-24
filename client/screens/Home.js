import React, {Component} from 'react';
import { StyleSheet, Text, View } from 'react-native';
import StartButton from '../elements/buttons/StartButton';
import { MaterialIcons as Icon } from '@expo/vector-icons';

export default class Home extends Component {
  static navigationOptions = {
    header: null,
  }

  render() {
    return (
      <View style={{flex:1, backgroundColor: '#1c73ff',}}>
        <View style={styles.placeTitle}>
          <Text style={styles.title}>Party Detectives</Text>
        </View>
        <View style={styles.search}>
          <Icon
            name="search"
            color='#fff'
            size={100}
            />
        </View>
        <View style={styles.button}>
          <View style={{flex: 1}} />
          <StartButton
            onPress = {() => this.props.navigation.navigate('Form')}
            />
          <View style={{flex: 1}} />
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  placeTitle: {
    flex: 2,
    alignItems: 'center',
    justifyContent: 'flex-end',
  },
  title: {
    fontSize: 60,
    fontWeight: 'bold',
    color: '#fff',
    textAlign: 'center',
  },
  button: {
    flex: 2,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'flex-start',
  },
  search: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
