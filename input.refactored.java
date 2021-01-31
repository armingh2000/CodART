package org.argouml.sequence2;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.argouml.moduleloader.ModuleInterface;
import org.argouml.notation.Notation;
import org.argouml.notation.NotationName;
import org.argouml.notation.NotationProviderFactory2;
import org.argouml.notation.providers.uml.SDMessageNotationUml;
import org.argouml.persistence.PersistenceManager;
import org.argouml.sequence2.diagram.SequenceDiagramFactory;
import org.argouml.uml.diagram.DiagramFactory;
import org.argouml.uml.diagram.DiagramFactory.DiagramType;
import org.argouml.uml.diagram.DiagramFactoryInterface2;

public class SequenceDiagramModule implements ModuleInterface {

    private static final Logger LOG =
        Logger.getLogger(SequenceDiagramModule.class.getName());

    private SequenceDiagramPropPanelFactory PPT;

    public boolean enable() {

        PPT =
            new SequenceDiagramPropPanelFactory();
        PropPanelFactoryManager.addPropPanelFactory(PPT);
        // TODO: Remove the casting to DiagramFactoryInterface2
        // as soon as DiagramFactoryInterface is removed.
        DiagramFactory.getInstance().registerDiagramFactory(
                DiagramType.Sequence,
                (DiagramFactoryInterface2) new SequenceDiagramFactory());

        NotationProviderFactory2 npf = NotationProviderFactory2.getInstance();
        NotationName nn = Notation.findNotation(Notation.DEFAULT_NOTATION);
        npf.addNotationProvider(NotationProviderFactory2.TYPE_SD_MESSAGE,
                nn, SDMessageNotationUml.class);

        PersistenceManager persistanceManager =
            PersistenceManager.getInstance();

        // Translate any old style sequence diagrams
        persistanceManager.addTranslation(
                "org.argouml.uml.diagram.sequence.ui.UMLSequenceDiagram",
                "org.argouml.sequence2.diagram.UMLSequenceDiagram");
        persistanceManager.addTranslation(
                "org.argouml.uml.diagram.sequence.ui.FigCreateActionMessage",
                "org.argouml.sequence2.diagram.FigMessage");

        LOG.log(Level.INFO, "SequenceDiagram Module enabled.");
        return true;
    }

    public boolean disable() {

        PropPanelFactoryManager.removePropPanelFactory(PPT);

        // TODO: Remove the casting to DiagramFactoryInterface2
        // as soon as DiagramFactoryInterface is removed.
        DiagramFactory.getInstance().registerDiagramFactory(
                DiagramType.Sequence, (DiagramFactoryInterface2) null);

        LOG.log(Level.INFO, "SequenceDiagram Module disabled.");
        return true;
    }

    public String getName() {
        return "ArgoUML-Sequence";
    }

    public String getInfo(int type) {
        switch (type) {
        case DESCRIPTION:
            return "The new sequence diagram implementation";
        case AUTHOR:
            return "Christian L\u00f3pez Esp\u00ednola";
        case VERSION:
            return "0.28";
        case DOWNLOADSITE:
            return "http://argouml-sequence.tigris.org";
        default:
            return null;
        }
    }
}

class SequenceDiagramPropPanelFactory implements PropPanelFactory {

    public PropPanel createPropPanel(Object object) {
        if (object instanceof UMLSequenceDiagram) {
            return new PropPanelUMLSequenceDiagram();
        }
        return null;
    }

    class PropPanelUMLSequenceDiagram extends PropPanelDiagram {


        public PropPanelUMLSequenceDiagram() {
            super(Translator.localize("label.sequence-diagram"),
                    lookupIcon("SequenceDiagram"));
        }

    }
}