import fetch from 'cross-fetch'

/* API CALLS ARE:
Recognition:
  - Want to recieve an image, and predicted label, maybe also another identifier for image
  - Returns: image, predicted label, and yes/no whether person thought that was right or not


Grammar:
  - Recieves two images, and a grammar
  - Populates and creates task based on grammar
  - Returns full tree of grammar chosen


Click Image:
  - Receive image, name of attribute, question to ask about attribute?
  - Returns: image name/identifier, name of attribute, pixel location for attribute, and boolean whether or not attribute exists in image

Choose Image:
  - Receives two images, an adverb and an adjective
  - Returns images, selected image, and attributes



*** GET ***
Send requests to:
/api/getRecognition
/api/getGrammar
/api/getClick
/api/getChoose


*** POST ***
Send Data to:
/api/postRecognition
/api/postGrammar
/api/postClick
/api/postChoose
which further break down in the backend

*/
export const API = 'http://localhost:5000';

export const RECOGNITION_API = '/recognitionTask';

export const GRAMMAR_API = '/grammarTask';

export const CLICK_API = '/clickTask';

export const CHOOSE_API = '/chooseTask';

export function getAPI(urls){
	return fetch(API + urls, {
		method: "get",
		headers: {
			'Content-Type': 'application/json'
		}
	})
	.then(response => response.json())
    //.then(data => this.setState({ data: data }));
}

export function postAPI(urls, data){
	return fetch(API + urls, {
		method: "post",
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data),
	})
	.then(response => response.json());
}


