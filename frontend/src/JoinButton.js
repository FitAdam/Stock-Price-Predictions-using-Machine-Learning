import react from 'react'
import { Button } from 'react-bootstrap';

function JoinButton() {
    return (
        <div>
            <style type="text/css">
                {`
    .btn-flat {
      background-color: blue;
      color: white;
    }

    .btn-xxl {
      padding: 1rem 1.5rem;
      font-size: 1.5rem;
    }
    `}
            </style>

            <Button variant="flat" size="xxl">
                Join now!
            </Button>
        </div>

    )
}

export default JoinButton