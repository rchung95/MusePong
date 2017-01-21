using UnityEngine;
using System.Collections;

public class PlayerControl : MonoBehaviour {
	public KeyCode moveUp = KeyCode.W;
	public KeyCode moveDown = KeyCode.S;
	public float speed = 10.0f;
	private Rigidbody2D rb2d;

	void Start () {
		rb2d = GetComponent<Rigidbody2D>();
	}

	void Update () {
		var reset = rb2d.velocity;
		reset.x = 0;
		rb2d.velocity = reset;

		if (Input.GetKey(moveUp))
		{
			var vel = rb2d.velocity;
			vel.y = speed;
			rb2d.velocity = vel;
		} else if (Input.GetKey(moveDown))
		{
			var vel = rb2d.velocity;
			vel.y = -1 * speed;
			rb2d.velocity = vel;
		} else if (!Input.anyKey)
		{
			var vel = rb2d.velocity;
			vel.y = 0.0f;
			rb2d.velocity = vel;
		}
	}
}