import React, {Component} from 'react';
import { ActivityIndicator, StyleSheet, Text, View } from 'react-native';
import TextButton from '../elements/buttons/TextButton';

export default class Wait extends Component {
  static navigationOptions = {
    header: null,
  }

  state = {
    isLoading: true,
  }

  socket = this.props.navigation.state.params.socket;


  sendAnswer(answer){
    this.socket.emit("wyr_answer", {
      answer: answer
    });
    this.setState({isLoading:true});
  }

  render() {
    if(this.state.isLoading){
      this.socket.on('wyr_ask', (data) => {
        let json = data.json();
        this.setState({questions: json, isLoading: false});
      });
      return(
        <View style={styles.loading}>
          <Text style={styles.text}>Loading Game ...</Text>
          <ActivityIndicator size = "large" color = "#1c73ff"/>
        </View>
      )
    }

    return (
      <View>
        <View style = {styles.loading}>
          <Text style = {styles.text}>Would you rather ?</Text>
        </View>
        <View style={styles.containerButton}>
          <TextButton
            onPress = { this.sendAnswer("A")}
            text = {this.state.questions.A}
            />
          <View style = {{flex:1}}/>
          <TextButton
            onPress = {this.sendAnswer("B")}
            text = {this.state.questions.B}
            />
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  loading: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    fontSize: 40,
    fontWeight: 'bold',
    color: '#1c73ff',
    textAlign: 'center',
  },
  containerButton: {
    flex: 1
  }
});
